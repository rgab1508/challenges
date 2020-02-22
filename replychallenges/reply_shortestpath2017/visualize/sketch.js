let file;
let START_X, START_Y, STOP_X, STOP_Y;
let N;
let obs = [];
let mObs = [];
let MAX_X, MAX_Y, MIN_X, MIN_Y;

function preload() {
	file = loadStrings('../inputs/input_4.txt');
}

function getMaxAndMin(file) {
	// console.log(file.length);
	let maxX = 0,
		maxY = 0,
		minX = Infinity,
		minY = Infinity;
	for (let i = 0; i < file.length; i++) {
		if (i == 1) {
			continue;
		}
		let line = file[i].split(' ');
		for (let j = 1; j < line.length + 1; j++) {
			if (j % 2 != 0) {
				//x stuff0
				if (parseInt(line[j - 1]) > maxX) {
					maxX = line[j - 1];
				}
				if (parseInt(line[j - 1]) < minX) {
					minX = line[j - 1];
				}
			} else {
				//y stuff
				if (parseInt(line[j - 1]) > maxY) {
					maxY = line[j - 1];
				}
				if (parseInt(line[j - 1]) < minY) {
					minY = line[j - 1];
				}
			}
		}
	}
	return [maxX, maxY, minX, minY];
}

function mapObs(obs) {
	let mObs = [];
	for (let i = 0; i < obs.length; i++) {
		ls = [];
		let l = obs[i];
		for (let j = 1; j < l.length + 1; j++) {
			let num;
			if (j % 2 != 0) {
				num = map(l[j - 1], MIN_X, MAX_X, 0, width);
			} else {
				num = map(l[j - 1], MIN_Y, MAX_Y, 0, height);
			}
			ls.push(num);
		}
		mObs.push(ls);
	}
	return mObs;
}

function setup() {
	let c = createCanvas(600, 600);
	let minMax = getMaxAndMin(file);
	// console.log(minMax);
	MAX_X = minMax[0];
	MAX_Y = minMax[1];
	MIN_X = minMax[2];
	MIN_Y = minMax[3];
	let l1 = file[0].split(' ').map(x => parseInt(x));
	START_X = map(l1[0], MIN_X, MAX_X, 0, width);
	START_Y = map(l1[1], MIN_Y, MAX_Y, 0, height);
	STOP_X = map(l1[2], MIN_X, MAX_X, 0, width);
	STOP_Y = map(l1[3], MIN_Y, MAX_Y, 0, height);
	N = file[1];

	// console.log(MAX_X, MAX_Y, MIN_X, MIN_Y, START_X, START_Y, STOP_X, STOP_Y);
	for (let i = 2; i < file.length; i++) {
		let vertexs = file[i].split(' ');
		obs.push(vertexs);
	}

	mObs = mapObs(obs);
	// console.log(mObs);
	background(51);
	// stroke(255);
	// fill(255, 0, 0);
	noStroke();
	// strokeWeight(2);
	for (let i = 0; i < mObs.length; i++) {
		beginShape();
		for (let j = 0; j <= mObs[i].length; j += 2) {
			let x = mObs[i][j];
			let y = mObs[i][j + 1];
			// console.log(x, y);
			vertex(x, y);
		}
		endShape(CLOSE);
	}
	// stroke(0, 200, 10);
	// strokeWeight(5);
	// point(START_X, START_Y);
	// stroke(200, 0, 10);
	// strokeWeight(5);
	// point(STOP_X, STOP_Y);
}
