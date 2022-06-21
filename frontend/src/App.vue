<template>
<div >

 <router-link to="/home"></router-link>

  <router-view></router-view>

  </div>
</template>

<script>


export default {

  name: 'App',
  data(){

    return{
    }

  },
  

}

</script>

<style>

a {

  /* Style from https://www.w3schools.com/css/css3_buttons.asp */
  border: none;
  padding: 15px;
  text-align: left;
  text-decoration: none;
  font-size: 10px;
}

/* a.router-link-active {
  background-color: gray;

} */
  .font{
     color: #111; 
     font-family: 'Open Sans', sans-serif; 
     font-size: 30px; 
     font-weight: 300; 
     line-height: 32px; 
     margin: 0 0 72px; 
     text-align: center;
     display: inline-block;

  }

.button {

  border: none;
  color: white;
  padding: 16px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  transition-duration: 0.4s;
  cursor: pointer;

  font-family: 'Helvetica Neue', sans-serif; 
  font-size: 30px; 
  font-weight: bold; 

  

}
.button5 {
  background-color: #555555;
  color: white;
  border: 2px solid #555555;
}

.button5:hover {
  background-color:white;
  color: black;
}

.demo-wrap {

  content: ' ';
  background: url("/src/assests/wom3.jpg");
  background-size: 50%; 
  background-repeat: no-repeat;
  background-position: calc(100% - 10px) center;
  width: 1480px;
  height: 450px;

 }

.text1 {
  margin: auto;
  width: 60%;
  padding: 100px;
  position: relative;
  text-align: left;
  color:black;
  font-family: 'Helvetica Neue', sans-serif; 
  font-size: 100px; 
  font-weight: bold; 
  letter-spacing: -1px; 
  line-height: 1; 
}

  .text2{
 color: rgb(0, 0, 0); 
 font-family: 'Open Sans Condensed', sans-serif; 
 font-size: 20px; 
 font-weight: 700; 
 line-height: 48px; 
 margin: 0 0 24px; 
 padding: 0 30px; 
 text-align: center;
  }




</style>
