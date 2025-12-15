import {useMutation, useQueryClient} from "@tanstack/react-query";
import {getPresignedURL, uploadToS3, saveMediaRecord} from "../api/media"


export default function UploadButton(){
    const queryClient = useQueryClient();

    const uploadMutation = useMutation({
        mutationFn : async (file) =>{
            // ask django for prsigned URL
            const {upload_url, raw_key} = await getPresignedURL(file);
            console.log("Presigned URL:", upload_url);
            console.log("Raw key:", raw_key);
                  // 2. Upload file to S3 WITH PUT REQUEST
            await uploadToS3(upload_url, file);

            console.log("Upload to S3 done.");

            // 3. Tell Django a media object should be created
            await saveMediaRecord(raw_key, file.name);

            console.log("Database updated.");
        },
        onSuccess : () =>{
            // refresh feed when upload is done
            queryClient.invalidateQueries({ queryKey: ["posts"] });
        },
    });
    const handleFileSelect = (e) =>{
        const file = e.target.files[0];
        if(!file) return;
        uploadMutation.mutate(file);
    };
    return (
        <div>
            <input type="file" onChange={handleFileSelect}/>
            {uploadMutation.isPending && <p>Uploading...</p>}
        </div>
    )
}