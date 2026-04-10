using System;

class Program
{
    static void Main()
    {
        string input = "12345";
        int total = 0;

        for (int i = 0; i < input.Length; i++)
        {
            total += input[i] - '0';   // <-- FIXED
        }

        Console.WriteLine("Total: " + total);

        Console.WriteLine("Finished calculation");
    }
}