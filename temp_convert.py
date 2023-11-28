#!/usr/bin/env python3
# Created By: Alex M
# Date: nov 5, 2023

def fahrenheit():
        degrees_Celsius = float(input("Enter degree in Celsius"))
        degrees_fahrenheit = 9/5 * degrees_Celsius + 32

        print(f"{degrees_Celsius} degrees Celsius in fahrenheit is {degrees_fahrenheit} ")

def main():
        
    fahrenheit()


if __name__ == "__main__":
        main()
