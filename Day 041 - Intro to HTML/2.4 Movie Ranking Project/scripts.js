document.addEventListener("DOMContentLoaded", function () {
    fetch('movies.json')
        .then(response => response.json())
        .then(movies => {
            const container = document.getElementById('movies-container');
            movies.forEach(movie => {
                const movieElement = document.createElement('div');
                movieElement.classList.add('movie');

                movieElement.innerHTML = `
                    <h3>${movie.title}</h3>
                    <img src="${movie.image}" alt="${movie.title}" class="movie-image"/>
                    <p>${movie.description}</p>
                    <p><strong>Rating:</strong> ${movie.rating}</p>
                `;

                container.appendChild(movieElement);
            });
        })
        .catch(error => console.error('Error loading movie data:', error));
});