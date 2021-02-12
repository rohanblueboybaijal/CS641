// C++ program for the above approach 

#include <bits/stdc++.h> 
using namespace std; 

// Function to implement the extended 
// euclid algorithm 
int gcd_extend(int a, int b, 
			int& x, int& y) 
{ 
	// Base Case 
	if (b == 0) { 
		x = 1; 
		y = 0; 
		return a; 
	} 

	// Recursively find the gcd 
	else { 
		int g = gcd_extend(b, 
						a % b, x, y); 
		int x1 = x, y1 = y; 
		x = y1; 
		y = x1 - (a / b) * y1; 
		return g; 
	} 
} 

// Function to print the solutions of 
// the given equations ax + by = c 
void print_solution(int a, int b, int c) 
{ 
	int x, y; 
	if (a == 0 && b == 0) { 

		// Condition for infinite solutions 
		if (c == 0) { 
			cout 
				<< "Infinite Solutions Exist"
				<< endl; 
		} 

		// Condition for no solutions exist 
		else { 
			cout 
				<< "No Solution exists"
				<< endl; 
		} 
	} 
	int gcd = gcd_extend(a, b, x, y); 

	// Condition for no solutions exist 
	if (c % gcd != 0) { 
		cout 
			<< "No Solution exists"
			<< endl; 
	} 
	else { 

		// Print the solution 
		cout << "x = " << x * (c / gcd) 
			<< ", y = " << y * (c / gcd) 
			<< endl; 
	} 
} 

// Driver Code 
int main(void) 
{ 
	int a, b, c; 

	// Given coefficients 
	a = 2021; 
	b = 9189; 
	c = -324; 

	// Function Call 
	print_solution(a, b, c); 

	a = 324;
	b = 2345;
	c = -9512;

	print_solution(a,b,c);
	return 0; 
} 
