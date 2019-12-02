// 예전 방식
var colors = ['red', 'orange', 'yello']
for (var i = 0; i < colors.length; i++){
  console.log(colors[i])
}

// use forEach
const COLORS = ['red', 'orange', 'yellow']
// COLORS.forEach(function(color){
//   console.log(color)
// })
let result = COLORS.forEach(color => console.log(color))
console.log(result)

// -------------------------------

// 실습 넘버1
function handlePosts(){
  const posts = [{
    id:23,
    title: "오늘의 뉴스"
  },
  {
    id:34,
    title: "오늘의 스포츠",
  },
  {
    id:78,
    title: "오늘의 연예"
  }]

  // forEach로 바꿔보자.
  // for(let i = 0; i < posts.length ; i++){
  //   console.log(posts[i])
  //   console.log(posts[i].id)
  //   console.log(posts[i].title)
  // }
  posts.forEach(function(post){
    console.log(post)
    console.log(post.id)
    console.log(post.title)
  })
}
handlePosts()







// 실습 2
// image 배열 안에 있는 정보를 가지고 
// 넓이를 구하고 그 값을 areas에 저장해보자
const IMAGES =[
  { height:10, width:30},
  { height:22, width:37},
  { height:54, width:42},
]
let areas = []

IMAGES.forEach(img => areas.push(img.height * img.width))

console.log(areas)
