// Take CSRF from DOM
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


// Modal PopUp Info game open
document.getElementById('open-modal').addEventListener('click', () => {
    document.getElementById('modal-info').style.display = 'block';
    document.getElementById('modal-info').style.opacity = 1;
});

// Modal PopUp Info game close
document.getElementById('close-modal').addEventListener('click', () => {
    document.getElementById('modal-info').style.display = 'none';
    document.getElementById('modal-info').style.opacity = 0;
});

// Modal PopUp end current game open
document.getElementById('open-endgame-modal').addEventListener('click', () => {
    document.getElementById('endgame-modal').style.display = 'block';
    document.getElementById('endgame-modal').style.opacity = 1;
});

click_active = true

// Loop for detect a click in a playbar 
const elements = document.querySelectorAll('.container-svg');

elements.forEach((element) => {
    element.addEventListener('click', function () {

        // deactivate game after click 
        if (click_active) {
            // Fetch for get a computer choice, set svg for display a choices and return a winner to django
            fetch(`/api-choise/`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
            })
                .then(response => {
                    response.json().then(choice => {

                        // Loop for reset all svg hands in page
                        document.querySelectorAll('.icon-reset').forEach((svg) => {
                            svg.style.display = 'none';
                        });

                        // set svg hand for user select
                        document.getElementById(element.getAttribute('data-svg-uman')).style.display = 'block';

                        // set svg hand for ai select
                        document.getElementById(choice.choice).style.display = 'block';



                        // send result to backend
                        fetch(`/api-result/`, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                                'X-CSRFToken': csrftoken
                            },
                            body: JSON.stringify({
                                'game': document.getElementById('gameId').value,    // get a game id from hidden imput
                                'player': element.getAttribute('data-svg-uman'),    // get a player choice
                                'computer': choice.choice                           // get a computer choice
                            })
                        })
                            .then(response => {

                                // Update result in a player cards
                                response.json().then(file => {
                                    
                                    document.querySelectorAll('.win').forEach((item) => {
                                        item.innerHTML = file.win;
                                    });
                                    document.querySelectorAll('.tie').forEach((item) => {
                                        item.innerHTML = file.tie;
                                    });
                                    document.querySelectorAll('.lost').forEach((item) => {
                                        item.innerHTML = file.lost;
                                    });

                                    click_active = false

                                    // Set title of result
                                    document.getElementById('gameResultText').innerHTML = file.str

                                    // display a form to try again
                                    document.getElementById('gameFrame').style.display = 'flex'
                                    document.querySelectorAll('.icon-reset').forEach((img) => {
                                        img.style.cursor = 'not-allowed';
                                    });
                                });
                            })
                            .catch(error => {
                                console.log(error);
                            });
                    });
                })
                .catch(error => {
                    console.log(error);
                });
        }
    });

});


// reset game
document.getElementById('brtRetry').addEventListener('click', () => {

    click_active = true

    document.getElementById('gameFrame').style.display = 'none'

    document.querySelectorAll('.icon-reset').forEach((img) => {
        img.style.cursor = "pointer";
    });

})



// Registration of the closing of the game
document.getElementById('close-modal-endgame').addEventListener('click', () => {

    // Get a play id
    const gameId = document.getElementById('gameId').value

    // Send a request
    fetch(`/closegame/${gameId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken // Includi il token CSRF nell'header della richiesta
        },
    })
        .then(response => {
            // Redirect to home
            window.location.reload();
        })
        .catch(error => {
            console.log(error)
        });
})










