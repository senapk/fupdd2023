let tam = 0;
let direcao = 1;
let cx = 100;
let cy = 100;

function setup() {
    createCanvas(400, 400);
}

function coracao(x, y, t) {
    let iniciox = x - t * 0.5
    let inicioy = y - t * 0.5
    //square(iniciox, inicioy, t);
    
    let ax = x;
    let ay = y;

    let bx = x;
    let by = y - t * 0.2;

    let cx = x - t * 0.8
    let cy = y - t * 0.5
    let ex = x + t * 0.8
    let ey = y - t * 0.5

    let dx = x;
    let dy = y + t * 0.4;
    noStroke();
    fill(255, 0, 0);
    bezier(bx, by, cx, cy, dx, dy, dx, dy)
    bezier(bx, by, ex, ey, dx, dy, dx, dy)
}

function draw() {
    fill(0, 0, 0, 10);
    square(0, 0, 400);
    tam += direcao;
    fill("red")
    coracao(100, 100, 200 - tam);
    coracao(200, 200, 100 + tam);
    if (tam > 100) {
        direcao = -2;
    }
    if (tam < 0) {
        direcao = 5;
    }
}