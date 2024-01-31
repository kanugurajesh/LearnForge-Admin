"use client";

import { UploadButton } from "@/utils/uploadthing";
import { useState } from "react";
import toast, { Toaster } from "react-hot-toast";

export default function Home() {
  const [fileUrl, setFileUrl] = useState<string | null>(null);
  const [fileName, setFileName] = useState<string | null>(null);

  const handleFileName = (e: any) => {
    setFileName(e.target.value);
  }

  const handleSubmit = async () => {
    const res = await fetch("/api/upload", {
      method: "POST",
      body: JSON.stringify({
        url: fileUrl,
        name: fileName,
      }),
    });
    const data = await res.json();
    console.log(data);
  }

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 gap-5">
      <Toaster />
      <UploadButton
        endpoint="imageUploader"
        onClientUploadComplete={(res) => {
          // Do something with the response
          setFileUrl(res[0].url as string);
          toast.success("Upload successful!");
        }}
        onUploadError={(error: Error) => {
          // Do something with the error.
          toast.error(`ERROR! ${error.message}`);
        }}
      />
      {fileUrl && (
        <img src={fileUrl} alt="Uploaded Image" className="w-40 h-40" />
      )}
      <input type="text" className="border-black border-2 rounded-md p-1 pl-2 pr-2" placeholder="Enter the Filename" onChange={handleFileName}/>
      <button className="bg-black text-white p-2 pl-6 pr-6 rounded-sm font-medium shadow hover:shadow-2xl">Submit</button>
    </main>
  );
}
