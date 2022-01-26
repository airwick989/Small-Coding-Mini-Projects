/*
Rocket Flight Calculator
*/

#include <iostream> //required for cout and endl
#define _USE_MATH_DEFINES  //required for pi constant
#include <math.h>
#include <cmath>	//required for mathematical operations
#include <iomanip>  //required to format output
#include <time.h>	//required to use time

using namespace std;

int main() {

	//declare and initialize objects
	double angle, a, ay, ax, t1, t2, t3, t_total, y1, y2, ymax, x1, x2, x_total, x_speed_max, thrust_speed_max, fall_speed_max;

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

		//Ask the user to enter corresponding Values within given parameters and ensures values are correct

		//Launch Angle
	cout << "Please enter the angle of launch in degrees (between 30 and 90, inclusive): " << endl;
	cin >> angle;

	while (angle < 30 || angle > 90) {
		cout << "This value is not within the parameters, please enter a correct launch angle: " << endl;
		cin >> angle;
	}

	//convert degrees to radians
	angle = (angle * M_PI) / 180;

	cout << endl;

	//Thrust Acceleration
	cout << "Now Please enter the acceleration of thrust in m/s^2 (between 30 and 100, inclusive): " << endl;
	cin >> a;

	while (a < 30 || a > 100) {
		cout << "This value is not within the parameters, please enter a correct thrust acceleration: " << endl;
		cin >> a;
	}

	cout << endl;

	//Thrust Time
	cout << "Now Please enter the length of time for thrust in seconds (between 30 and 150, inclusive): " << endl;
	cin >> t1;

	while (t1 < 30 || t1 > 150) {
		cout << "This value is not within the parameters, please enter a correct length of thrust time: " << endl;
		cin >> t1;
	}

	cout << endl;

	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

		//Calculations

		//Acceleration in the y direction during thrust
	ay = a * sin(angle);

	//Acceleration in the x direction during thrust
	ax = a * cos(angle);

	//Height reached during thrust
	y1 = 0.5 * ay * t1 * t1;

	//Max vertical speed reached during thrust
	thrust_speed_max = sqrt(2 * ay * y1);

	//Vertical distance travelled during coast upwards
	y2 = (thrust_speed_max * thrust_speed_max) / (2 * 9.8);

	//Time spent coasting upwards
	t2 = thrust_speed_max / 9.8;

	//Max height reached
	ymax = y1 + y2;

	//Max vertical speed upon decent
	fall_speed_max = sqrt(2 * 9.8 * ymax);

	//Time spent falling
	t3 = fall_speed_max / 9.8;

	//Entire time of flight
	t_total = t1 + t2 + t3;

	//Horizontal distance travelled during thrust
	x1 = 0.5 * ax * t1 * t1;

	//Maximum speed reached travelling horizontally
	x_speed_max = sqrt(2 * ax * x1);

	//Horizontal distance travelled during coast
	x2 = x_speed_max * (t2 + t3);

	//Total horizontal distance travelled
	x_total = x1 + x2;

	cout << endl;
	//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

		//Output necessary results

		//Convert angle back to degrees
	angle = (angle * 180) / M_PI;

	cout << "Launch angle entered: " << angle << " degrees" << endl;
	cout << "Acceleration of thrust entered: " << a << " m/s^2" << endl;
	cout << "Length of thrust time entered: " << t1 << " seconds" << endl;

	//Rounds final answers to 3 significant figures
	cout << setprecision(3);

	cout << endl << "The rocket will achieve a maximum altitude of " << ymax << " meters and travel total a horizontal distance of " <<
		x_total << " meters" << endl;


	//exit program
	return 0;
}