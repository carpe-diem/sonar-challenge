import { useState, useEffect } from 'react';
import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import axios from 'axios';
import Post from '../components/Post';



export default function Home() {
  const [postList, setPostList] = useState([]);

  const getPostList = () => {
    let config = {
      headers: {
        'Authorization': 'Bearer ' + sessionStorage.getItem('token')
      }
    }
    axios.get("http://127.0.0.1:8000/posts", config).then((res) => {
      const Post = res.data;
      setPostList(Post);
    });
  };
  
  useEffect(() => {
    if (!sessionStorage.getItem('token')){
      router.push('/login');
    }
    else{
      getPostList()
    }

  }, []);

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Posts</h1>

      <main className={styles.main}>
      {
        postList.map((post, index) => 
          <Post key={post.id} title={post.tile} img={post.imageSrc} id={post.id}/>
        )
      }
      </main>


    </div>
  )
}
