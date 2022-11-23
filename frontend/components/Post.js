import styles from './Post.module.css'
import Image from 'next/image'

const Post = (props) => {

    const handleChange = (e)=>{
        // TODO
    };

    return(
        <div className="l-container">
            <div className="l-grid l-grid-col3">
                <ul className="l-grid">
                    <li className="l-grid-item">
                        <article className="post">
                        <a classNameName="post-link" href={`/post/${props.id}`}>
                            <Image
                                src={props.img}
                                alt={props.title}
                                width={50}
                                height={50}
                                className={styles.post_img}
                                priority
                            />
                        
                                <h1 className="post-heading">
                                sample sample sample v sample sample sample sample 
                                </h1>
                            </a>
                            
                            <div className="post-like">
                            <dl className="like">
                                <dt>
                                {/* <img src="" alt=""> */}
                                </dt>
                                <dd>
                                <a onClick="handleLike">Like</a>
                                </dd>
                            </dl>
                            </div>
                       
                        </article>
                    </li>
                
                </ul>
            </div>
        </div>
    )
}

export default Post;




