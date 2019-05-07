
#include <opencv2/opencv.hpp>

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
}



