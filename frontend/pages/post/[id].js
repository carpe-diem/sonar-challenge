import Image from 'next/image'
import { useState, useEffect } from 'react';
import axios from 'axios';
import { useRouter } from 'next/router'


const PostDetail = () => {
    const router = useRouter()
    const [postList, setPostList] = useState();
    const [postId, SetPostId] = useState();

    
    const getPost = () => {
        let config = {
          headers: {
            'Authorization': 'Bearer ' + sessionStorage.getItem('token')
          }
        }
        
        if (postId != undefined){
            console.log("xxx",postId)
            axios.get(`http://127.0.0.1:8000/post/${postId}`, config).then((res) => {
            const Post = res.data;
            setPostList(Post);
            });
        }
      };
      
      useEffect(() => {
        SetPostId(router.query.id)
        if (!sessionStorage.getItem('token')){
          router.push('/login');
        }
        else{
          getPost()
        }
    
        }, []);

    return(
        <div className="l-container">
            <div className="l-grid l-grid-col3">
                <ul className="l-grid">
                    <Image
                        src={postList.imageSrc}
                        alt={postList.title}
                        width={200}
                        height={200}
                        priority
                    />
                    <h1 className="post-heading">{postList.title}</h1>
                    <p className="post-heading">{postList.description}</p>
                    <h4 className="post-heading">Likes: {postList.likes}</h4>
                </ul>
            </div>
        </div>
    )
}

export default PostDetail;




