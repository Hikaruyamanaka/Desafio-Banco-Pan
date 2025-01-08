// Array Rotation
// This challenge is about moving numbers around in a list. It's useful for rearranging data.

// The Problem: You have a list of numbers. You need to move the numbers to the right by a certain amount. The user will tell you how many times.
// Example:
// Input list: [1, 2, 3, 4, 5] 
// Shifts: 2
// Output list: [4, 5, 1, 2, 3]

// Seu input para o desafio será: 
// Array: 1, 2, 3, 4, 5, 6, 7
// Shifts: 4


using System;

class Program 
{
    static void Main() 
    {

        Console.WriteLine("\n-+-+-+-+-+-+-   DESAFIO 02   -+-+-+-+-+-+-\n");

        int[] array = { 1, 2, 3, 4, 5, 6, 7 };
        int rotacoes = 4;

        // Rotacionar o array
        int[] arrayRotacionado = new int[array.Length];

        for (int i = 0; i < array.Length; i++) 
        {
            // Calcular nova posição
            int novaPosicao = (i + rotacoes) % array.Length;

            // Mover elemento
            arrayRotacionado[novaPosicao] = array[i];
        }

        // Imprimir o resultado
        Console.WriteLine("Saída: " + string.Join(", ", arrayRotacionado)); // string.Join serve para unir os elementos
    }
}

