// Find the Longest Word
// This coding challenge is all about working with words in a sentence. It's a good exercise to get better at handling text.

// The Problem: Your task is to write a function that looks at a sentence and figures out which word is the longest. Then, it tells you how many letters that word has.
// Example Input:
// "The quick brown fox jumped over the lazy dog"

// Example Output:
// 6 (because "jumped" is the longest word)
// Seu input para o desafio será: “Banco Pan, um banco completo com soluções inteligentes”


using System;

class Program {
    static void Main() {

        Console.WriteLine("\n-+-+-+-+-+-+-   DESAFIO 01   -+-+-+-+-+-+-\n");

        string sentence = "Banco Pan, um banco completo com soluções inteligentes";

        // Inicializa a variável da palavra mais longa
        string maiorPalavra = "";  

        // Inicializa a variável do comprimento da palavra mais longa
        int maxTamanho = 0;        

        // Divide a sentença em palavras
        string[] palavras = sentence.Split(' ');

        // Percorre todas as palavras
        foreach (string palavra in palavras) {

            // Verifica se o comprimento da palavra atual é maior que o comprimento máximo encontrado até agora
            if (palavra.Length > maxTamanho) {

                // Atualiza o comprimento máximo
                maxTamanho = palavra.Length;  

                // Atualiza a palavra mais longa
                maiorPalavra = palavra;       
            }
        }

        // Exibe a palavra mais longa: "inteligentes"
        Console.WriteLine("Saída: " + maiorPalavra);  
    }
}
