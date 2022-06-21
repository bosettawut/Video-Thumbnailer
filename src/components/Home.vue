<template>

<div class="demo-wrap" style="text-align:center;" >

  <h1 class="text1">katukjit-kachakjai.<br />

  <router-link to="/video">

  <button class="button button5">Let's start</button>

  </router-link>

  </h1>

</div>


</template>


<script>

export default {

  data() {
    return {
    };
  },
};

</script>


<style>

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
  font-size: 20px; 
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

.text1 {
  margin: auto;
  width: 60%;
  padding: 100px;
  position: relative;
  text-align: left;
  color:black;
  font-family: 'Helvetica Neue', sans-serif; 
  font-size: 30px; 
  font-weight: bold; 
  letter-spacing: -1px; 
  line-height: 1; 
}


</style>