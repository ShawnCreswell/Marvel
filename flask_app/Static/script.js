// const charactersList = document.getElementById('charactersList');
// const searchBar = document.getElementById('searchBar');
// let hpCharacters = [];
// console.log(searchBar);
// searchBar.addEventListener("keyup",(e) => {
//     const searchString = e.target.value;
//     const filteredCharacters = hpCharacters.filter( character => {
//         return character.name.contain(searchString) || character.house.contain(searchString);
//     });
//     console.log(filteredCharacters);
// });

// const loadCharacters = async () => {
//     try {
//         const res = await fetch('https://hp-api.herokuapp.com/api/characters');

//         hpCharacters = await res.json();
//         displayCharacters(hpCharacters);
//         console.log(hpCharacters)

//     } catch (err) {
//         console.error(err);
//     }
// };

// const displayCharacters = (characters) => {
//     const htmlString = characters
//         .map((character) => {
//             return `
//             <li class="character">
//                 <h2>${character.name}</h2>
//                 <p>House: ${character.house}</p>
//                 <img src="${character.image}"></img>
//             </li>
//         `;
//         })
//         .join('');
//     charactersList.innerHTML = htmlString;
// };

// loadCharacters();