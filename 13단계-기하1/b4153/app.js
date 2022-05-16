const fs = require("fs");
//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);

function solution(input) {
	for(let line of input) {
		let values = line.split(" ").map((item) => +item);
		
		if(values[0] === 0) {
			break;
		}
		values.sort((a,b) => {
			return a - b;
		});
		
		if((values[0] * values[0]) + (values[1] * values[1]) === (values[2] * values[2])) {
			console.log("right");
		} else {
			console.log("wrong");
		}
	}

}