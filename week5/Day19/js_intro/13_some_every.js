const NUMBERS = [1,2,3,4,5]

// some 
// 요소중에 하나라도 만족하는 값이 있다면 검색을 멈추고 true를 반환
const some_result = NUMBERS.some(function (elem){
  return elem % 2 === 0
})
console.log(some_result)

// every 
// 조건을 모든 요소들이 만족해야 true 를 반환
// 만족하지 않는 값이 있으면 검색을 그만두고 false를 반환
const every_result = NUMBERS.every(function (elem){
  return elem % 2 === 0
})
console.log(every_result)
