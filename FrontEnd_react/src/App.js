import "./App.css";
import { useEffect, useState } from "react";
const BASE_URL = "https://blog-fastapi-react.onrender.com";

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(
    function () {
      async function FetchPosts() {
        const result = await fetch(`${BASE_URL}/post/all`);
        const data = await result.json();
        setPosts(data);
        console.log(data);
      }
      FetchPosts();
    },
    [setPosts],
  );

  return (
    <div>
      <Posts posts={posts} />
      <BlogForm posts={posts} setPosts={setPosts} />
    </div>
  );
}
function Posts({ posts }) {
  return (
    <div className="App">
      {posts.map((post, i) => (
        <Post key={i} post={post} />
      ))}
    </div>
  );
}

function Post({ post }) {
  return (
    <article className="post-card">
      <h1 className="post-title">{post.title}</h1>

      {post.image_url && (
        <img
          className="post-image"
          src={`${post.image_url}`}
          alt={post.title}
        />
      )}

      <p className="post-content">{post.content}</p>

      <div className="post-author">{post.creator}</div>
    </article>
  );
}

function BlogForm({ posts, setPosts }) {
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [creator, setCreator] = useState("");
  const [image_url, setImage] = useState("");
  const handleUpload = async (e) => {
    const formData = new FormData();
    formData.append("image", e);
    for (const pair of formData.entries()) {
      console.log(pair[0], pair[1]);
    }
    const result = await fetch(`${BASE_URL}/post/image`, {
      method: "POST",
      body: formData,
    });

    const data = await result.json();
    setImage(data.filename);
  };
  function onsubmit(e) {
    e.preventDefault();
    async function Post() {
      const requestOptions = {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          image_url: image_url,
          title: title,
          content: content,
          creator: creator,
        }),
      };
      const resp = await fetch(`${BASE_URL}/post`, requestOptions);
      const data = await resp.json();
      console.log(data);
      setContent("");
      setCreator("");
      setTitle("");
      setPosts((c) => [
        ...c,
        {
          image_url: image_url !== "" ? image_url : "",
          title: title,
          content: content,
          creator: creator,
        },
      ]);
    }

    Post();
  }

  return (
    <div className="blog-container">
      <form className="blog" onSubmit={onsubmit}>
        <h2>Create Blog Post</h2>

        <div className="form-group">
          <label>Featured Image</label>
          <input
            type="file"
            onChange={(e) => handleUpload(e.target.files?.[0])}
          />
        </div>

        <div className="form-group">
          <label>Title</label>
          <input
            value={title}
            type="text"
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter title"
          />
        </div>

        <div className="form-group">
          <label>Content</label>
          <textarea
            value={content}
            onChange={(e) => setContent(e.target.value)}
            placeholder="Write your content..."
            rows="6"
          />
        </div>

        <div className="form-group">
          <label>Creator</label>
          <input
            value={creator}
            type="text"
            onChange={(e) => setCreator(e.target.value)}
            placeholder="Author name"
          />
        </div>

        <button type="submit">Publish Post</button>
      </form>
    </div>
  );
}
export default App;
