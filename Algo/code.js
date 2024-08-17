
function fizzBuzz(N) {
    // Vérifier que l'entrée est un nombre entier positif
    if (!Number.isInteger(N) || N <= 0) {
        console.error("Veuillez entrer un nombre entier positif.");
        return;
    }

    // Itérer de 1 à N
    for (let i = 1; i <= N; i++) {
        // Initialiser une chaîne de caractères pour le résultat
        let output = "";

        // Vérifier les conditions pour Fizz, Buzz ou FizzBuzz
        if (i % 3 === 0) output += "Fizz";
        if (i % 5 === 0) output += "Buzz";

        // Si aucune condition n'est remplie, utiliser le nombre lui-même
        console.log(output || i);
    }
}

// Exemple d'utilisation
fizzBuzz(15);

