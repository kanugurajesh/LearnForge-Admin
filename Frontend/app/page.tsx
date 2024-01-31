"use client";

import { UploadButton } from "@/utils/uploadthing";
import { useState } from "react";
import toast, { Toaster } from "react-hot-toast";

export default function Home() {
  const [fileUrl, setFileUrl] = useState<string | null>(null);
  const [fileName, setFileName] = useState<string | null>(null);

  const handleFileName = (e: any) => {
    setFileName(e.target.value);
  };

  const handleSubmit = async () => {
    if (!fileUrl) {
      toast.error("Please upload an image");
      return;
    }

    if (!fileName) {
      toast.error("Please enter a filename");
      return;
    }

    toast.loading("Processing...");

    const res = await fetch("/api/upload", {
      method: "POST",
      body: JSON.stringify({
        fileUrl,
        fileName,
      }),
    });

    const data = await res.json();

    toast.dismiss();

    if (data.error) {
      toast.error(data.error);
      return;
    }

    toast.success("Data upload successful!");
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24 gap-5">
      <Toaster />
      <UploadButton
        endpoint="imageUploader"
        onClientUploadComplete={(res) => {
          // Do something with the response
          setFileUrl(res[0].url as string);
          toast.success("Image upload successful!");
        }}
        onUploadError={(error: Error) => {
          // Do something with the error.
          toast.error(`ERROR! ${error.message}`);
        }}
      />
      {fileUrl && (
        <img src={fileUrl} alt="Uploaded Image" className="w-40 h-40" />
      )}
      <input
        type="text"
        className="border-black border-2 rounded-md p-1 pl-2 pr-2"
        placeholder="Enter the Filename"
        onChange={handleFileName}
      />
      <button
        className="bg-black text-white p-2 pl-6 pr-6 rounded-sm font-medium shadow hover:shadow-2xl"
        onClick={handleSubmit}
      >
        Submit
      </button>
    </main>
  );
}
