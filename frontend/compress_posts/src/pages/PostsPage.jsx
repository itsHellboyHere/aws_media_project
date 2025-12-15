import { useQuery } from "@tanstack/react-query";
import { getPosts } from "../api/media";
import UploadButton from "../components/UploadButton";

export default function PostsPage(){
    const{data,isLoading} = useQuery({
        queryKey:["posts"],
        queryFn: getPosts,
        // refetchInterval: 3000,
    });
    return(
        <div style={{padding: "20px"}}>
            <h2>My posts</h2>
            <UploadButton />
            {isLoading && <p>Loading posts...</p>}
            
      <div>
        {data?.map((post) => (
          <div key={post.id} style={{ marginBlock: 12 }}>
            <strong>{post.original_filename}</strong>
            <br />

            {/* show compressed image */}
            {post.file_url ? (
              <img
                src={post.file_url}
                alt=""
                style={{ width: 200, borderRadius: 8 }}
              />
            ) : (
              <p>Processing…</p>
            )}
          </div>
        ))}
      </div>
        </div>
    )
}