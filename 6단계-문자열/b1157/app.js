const fs = require("fs");

//const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
const filePath = "./input.txt";

// ? toLowerCase() => 소문자로 변환하는 method
let input = fs.readFileSync(filePath).toString().trim().toLowerCase();

solution(input);

function solution(value) {

   // Todo Array.fill로 배열 26개 만듬
   const result = new Array(26).fill(0);
   
   /*
   Todo input 값 loop 돌아서 아스키 코드로 변환해서 (a = 97) 
   Todo 일치하는 경우 배열에 숫자 증감
   */ 

   for(let i = 0; i < value.length; i++) {
      result[input.charCodeAt(i) - 97]++;
   }

   // Todo 26개 배열 중 가장 높은 값 찾고
   const max = Math.max(...result);
   // Todo 그 배열의 위치 값 추출
   const index = result.indexOf(max);

   let isSame = false;

   for(let j = 0; j < 26; j++) {
      if(result[j] === max && index != j) {
         isSame = true;
         break;
      }
   }
   // Todo 대문자 출력은 +65('A')부터 해줘야함
   console.log(isSame ? "?" : String.fromCharCode(index + 65));

}