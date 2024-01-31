import { NextRequest, NextResponse } from "next/server";

export async function POST(req: NextRequest) {
  const reqBody = await req.json();
  const { fileUrl, fileName } = reqBody;

  try {
    const BACKEND_URL = process.env.BACKEND_URL;

    const URL = BACKEND_URL + "/upload";

    const res = await fetch(URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ fileUrl, fileName }),
    });

    const data = await res.json();

    console.log(data);

    return NextResponse.json(
      { message: "Success", success: true },
      { status: 200 }
    );
  } catch (error) {
    return NextResponse.json(
      { message: "Failure", success: false },
      { status: 400 }
    );
  }
}
