<template>
<div>
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

<section class="page-content" style="text-align:center;">
  <section class="grid" style="text-align:center;">
 <h1 >ALL GIF (after delete please refresh)</h1>

        <v-col
        v-for="(d, index) in decode.All_GIF"
        :key="index"
        class="d-flex child-flex"
        cols="4"
      >
       <img v-bind:src="'data:image/jpeg;base64,'+ d" />
      {{index}}
      </v-col>

        <button class="button button5" @click="delete_all()" method="post">
            delete all 
        </button>
      
  </section>
</section>
</div>
</template>

<script>
import axios from "axios";


export default {
  
       mounted(){
        
          this.decodetoGIF()
      },

    data() {

      return{
          list_videos:[],
          decode:[]
      }
    },
 
    methods: {


   async decodetoGIF(){
    const path = 'http://localhost:80/list_gifs'
        console.log("GIF")
        axios.get(path)
        .then((response) =>{
          this.decode = response.data
          console.log(response.data)
          console.log(response.length)
    
   } ) .catch((err)=>{
          console.log(err);
          
        });
   },
   async delete_all(){
    const path = 'http://localhost:80/delete_gif'
        console.log("DELETE")
        axios.get(path)
   }
    
}
 
}

</script>

