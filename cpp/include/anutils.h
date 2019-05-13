#include <string>
#include <opencv2/opencv.hpp>
#include <xtensor/xarray.hpp>

namespace an 
{
	cv::Scalar hsvToRgbColor(float h, float s, float v, bool bgr = true)
	{		
		float C = v * s;
		float X = C * (1 - abs(fmod(h / 60, 2) - 1));
		float m = v - C;

		float erregebes[6][3] = { {C,X,0}, {X,C,0}, {0,C,X}, {0,X,C}, {X,0,C}, {C,0,X} };				
		float* rgb = erregebes[cvFloor(h / 60)];
				
		if (bgr)		
			return cv::Scalar(cvRound((rgb[2] + m) * 255), cvRound((rgb[1] + m) * 255), cvRound((rgb[0] + m) * 255));		
		else 		
			return cv::Scalar(cvRound((rgb[0] + m) * 255), cvRound((rgb[1] + m) * 255), cvRound((rgb[2] + m) * 255));

	}

	std::set<std::string> maisOuMenosColorName(xt::xarray<float> hagas)
	{
		std::set<std::string> color_names;
		for (float h : hagas)
		{
			std::string cor;
			if (h >= 0 && h <= 15)
				cor = "vemelho";
			else if (h > 15 && h <= 22)
				cor = "laranja";
			else if (h > 22 && h <= 30)
				cor = "amarelo";
			else if (h > 30 && h <= 37)
				cor = "amarelo";
			else if (h > 37 && h <= 60)
				cor = "verde";
			else if (h > 60 && h <= 75)
				cor = "verde";
			else if (h > 75 && h <= 90)
				cor = "magenta";
			else if (h > 90 && h <= 105)
				cor = "magenta";
			else if (h > 105 && h <= 120)
				cor = "azul";
			else if (h > 120 && h <= 135)
				cor = "roxo";
			else if (h > 135 && h <= 150)
				cor = "rosa";
			else if (h > 150 && h <= 165)
				cor = "rosa";
			else if (h > 165 && h <= 180)
				cor = "vermelho";
			
			color_names.insert(cor);
		}

		return color_names;
	}
}



