<template>
  <div id="app" style="text-align:center;">
<header class="page-header">
  <nav>
    <a href="#0" aria-label="forecastr logo" class="logo">
      <svg width="140" height="49">
        <use xlink:href="#logo"></use>
      </svg>
    </a>
    <button class="toggle-mob-menu" aria-expanded="false" aria-label="open menu">
      <svg width="20" height="20" aria-hidden="true">
        <use xlink:href="#down"></use>
      </svg>
    </button>

    <ul class="admin-menu">
      <li class="menu-heading">
        <h3>Menu</h3>
      </li>

      <li>
        <router-link to="/gif">
          <svg>
            <use xlink:href="#users"></use>
          </svg>
          <span>GIF</span>
        </router-link>
      </li>

      <li>
        <router-link to="/video">
          <svg>
            <use xlink:href="#trends"></use>
          </svg>
          <span >Home</span>
        </router-link>
      </li>

      <li>
        <router-link to="/status">
          <svg>
            <use xlink:href="#trends"></use>
          </svg>
          <span>Status</span>
        </router-link>
      </li>

      <li>
        <router-link to="/video">
          <svg>
            <use xlink:href="#trends"></use>
          </svg>
          <span >Back</span>
        </router-link>
      </li>  

    </ul>
  </nav>
</header>
  
<div style="text-align:center;">
        <input type="text" name="id" placeholder="Type here" v-model="id">
        <button class="button button5" @click="get_status(id)" method="post">
            Check status
        </button>
        
        
        {{this.status}}
</div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: 'app',

  data () {
    return {
      status:"",
      id:""
  
      }
  },
  methods: {
     async get_status(i){
      const data = { id:i };
        console.warn(data)
      await axios.post("http://localhost:80/get_status",data)
        .then((response) =>{
          this.status = response.data
          console.log(response.data)
        })
        .catch((err)=>{
          console.log(err);
         
        });
     },
     check(){
      console.warn(this.id)
     }
  }
}
  
   
</script>
<style>

::placeholder {
  color: red;
}
</style>
