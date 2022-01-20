// Main loop function
function timeMovesUniverse() {
    drawUniverse();  // Draw current state of universe
    updateUniverse();  // Update the universe
    requestAnimationFrame(timeMovesUniverse);  // Updates the screen whenever it's called to run GoL on infinite loop,
}                                             //passing 'timeMovesUniverse' into requestAnimationFrame calls itself infinitely

// Create a 2d array by creating an empty array of n elements, each of which contains another empty n elements array
function createArray(rows) {
    var array = [];
    for (var more_arrays = 0; more_arrays < rows; more_arrays++) {
        array[more_arrays] = [];
    }
    return array;
}

// Randomly populate the universe with 1s and 0s. Math.random returns a floating num b/w 1 and 0 so we need to call round on it
// Setting y and x to 100 and then subtracting that same amount from uni height/width centres uni on the canvas
function randomiseUniverse() {
    // Iterate through columns
    for (var y = 100; y < universeHeight - 100; y++) {
        // Iterate through rows
       for (var x = 100; x < universeWidth - 100; x++) {
           universe[y][x] = Math.round(Math.random());
       }
    }
}

// Draw the contents of universe onto canvas
function drawUniverse() {
    // Clear canvas before each redraw
    context.clearRect(0, 0, universeHeight, universeWidth);
    // Iterate through columns
    for (var y = 1; y < universeHeight; y++) {
        // Iterate through rows
        for (var x = 1; x < universeWidth; x++) {
            if (universe[y][x] === 1) {
                context.fillRect(y, x, 2, 2);  // determines nom size
            }
        }
    }
}

// Iterate once through a universe update
function updateUniverse() {
    // Iterate columns
    for (var y = 1; y < universeHeight - 1; y++) {
        // Iterate rows
        for (var x = 1; x < universeWidth - 1; x++) {
            // Sum total values for neighbouring cells
            var sumNeighbours = 0;
            sumNeighbours += universe[y - 1][x - 1];  // northwest
            sumNeighbours += universe[y - 1][x];      // north
            sumNeighbours += universe[y - 1][x + 1];  // northeast
            sumNeighbours += universe[y][x + 1];      // east
            sumNeighbours += universe[y + 1][x + 1];  // southeast
            sumNeighbours += universe[y + 1][x];      // south
            sumNeighbours += universe[y + 1][x - 1];  // southwest
            sumNeighbours += universe[y][x - 1];      // west

            // Apply rules to each nom
            switch (sumNeighbours) {
                case 2:
                    mirrorUniverse[y][x] = universe[y][x];  // stasis: 2 live nom neighbours means a dead nom stays
                    break;                                  // dead, a live nom keeps living.

                case 3:
                    mirrorUniverse[y][x] = 1;  // regeneration: if nom is dead and neighbours sum to 3, turn it on,
                    break;                     // living noms stay alive, so current nom is always alive

                default:
                    mirrorUniverse[y][x] = 0; // default is death b/c any other number (>2 or <3) of live nom neighbours
        }                                      // means the nom dies or stays dead
    }
}

// Swap universes to prevent state bug of universes not updating wholly at once after all changes applied
var tempUniverse = universe;
universe = mirrorUniverse;
mirrorUniverse = tempUniverse;
}

// All the initialising variables
var universeHeight = 600;
var universeWidth = 600;
var universe = createArray(universeWidth);
var mirrorUniverse = createArray(universeWidth);
var canvas = document.getElementById("golCanvas");
var context = canvas.getContext("2d");  // creates a CanvasRenderingContext2D object representing a 2d rendering context.
canvas.style.backgroundColor = '#000000'
context.fillStyle = '#0037FF';

// Initialise starting state for the uni by filling it with random noms
randomiseUniverse();

// Call the main loop
timeMovesUniverse();
