#pragma once

#include <opencv2/opencv.hpp>
#include <iostream>
#include <vars.h>
#include <anutils.h>
#include <xtensor/xarray.hpp>
#include <xtensor/xio.hpp>
#include <xtensor/xview.hpp>
#include <xtensor/xsort.hpp>

using namespace std;
using namespace cv;
using namespace xt::placeholders;

void predcolor(string imgPath)
{
	Mat img, hsv;
	img = imread(imgPath);
	cvtColor(img, hsv, COLOR_BGR2HSV);
	
	int histSize = 180;
	float range[] = { 0,180 };
	const float* histRange = { range };
	const int chanels[] = { 0 };
	MatND hist;
	calcHist(&hsv, 1, chanels, Mat(), hist, 1, &histSize, &histRange, true, false);
	
	int pw = 640, ph = 400;
	Mat histPlot(ph, pw, CV_8UC3, Scalar(0, 0, 0));
	normalize(hist, hist, 0, ph, NORM_MINMAX);

	int bw = cvRound(pw / histSize);

	xt::xarray<float> harray = xt::zeros<float>({ histSize });
		
	for (int i = 1; i < histSize; i++)
	{
		harray[i] = hist.at<float>(i);
		
		line(histPlot,
			Point( bw * (i-1), ph - cvRound(hist.at<float>(i-1))),
			Point(bw * i, ph - cvRound(hist.at<float>(i))),
			an::hsvToRgbColor((float)i*2,1,1), 1);
	}

	xt::xarray<float> topcolors = xt::view(xt::argsort(harray), xt::range(-3, _));
	auto colorNames = an::maisOuMenosColorName(topcolors);
		
	Point tpos(350, 50);
	for (string color : colorNames)
	{
		putText(histPlot, color, tpos, FONT_HERSHEY_SIMPLEX, 0.7, Scalar::all(200) , 1);		
		tpos.y += 30;
		cout << color << endl;
	}		

	imshow("original", img);
	imshow("histograma", histPlot);
	
	waitKey();
}

int main(int argc, char* argv[])
{		
	predcolor(GetImgFolder(argv) + "\\a1\\futebol.jpg");
	predcolor(GetImgFolder(argv) + "\\a1\\moda.jpg");	
	predcolor(GetImgFolder(argv) + "\\a1\\simpsons.jpeg");
}