// import React, { useState, useRef } from "react";

// const App = () => {
//   const [image, setImage] = useState(null);
//   const [audio, setAudio] = useState(null);
//   const [uploadedAudio, setUploadedAudio] = useState(null);
//   const [text, setText] = useState("");
//   const [audioUrl, setAudioUrl] = useState("");
//   const [videoUrl, setVideoUrl] = useState("");
//   const [isRecording, setIsRecording] = useState(false);
//   const mediaRecorderRef = useRef(null);
//   const audioChunksRef = useRef([]);

//   // Handle image selection
//   const handleImageChange = (event) => {
//     setImage(event.target.files[0]);
//   };

//   // Handle audio file selection
//   const handleAudioChange = (event) => {
//     setUploadedAudio(event.target.files[0]);
//     setAudio(null); // Reset recorded audio if a file is uploaded
//     setAudioUrl(""); // Clear any generated audio URL
//   };

//   // Handle text input
//   const handleTextChange = (event) => {
//     setText(event.target.value);
//   };

//   // Convert text to speech (TTS)
//   const generateTTS = async () => {
//     if (!text) {
//       alert("Please enter text to convert to speech.");
//       return;
//     }

//     try {
//       const response = await fetch("http://localhost:8000/generate_audio/", {
//         method: "POST",
//         body: new URLSearchParams({ text }),
//         headers: { "Content-Type": "application/x-www-form-urlencoded" },
//       });

//       const data = await response.json();
//       if (data.audio_url) {
//         setAudioUrl(data.audio_url);
//         setUploadedAudio(null); // Clear uploaded audio if TTS is used
//       } else {
//         alert("Failed to generate speech.");
//       }
//     } catch (error) {
//       console.error("TTS error:", error);
//     }
//   };

//   // Start recording audio
//   const startRecording = async () => {
//     try {
//       const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
//       mediaRecorderRef.current = new MediaRecorder(stream);
//       audioChunksRef.current = [];

//       mediaRecorderRef.current.ondataavailable = (event) => {
//         audioChunksRef.current.push(event.data);
//       };

//       mediaRecorderRef.current.onstop = () => {
//         const audioBlob = new Blob(audioChunksRef.current, { type: "audio/wav" });
//         setAudio(audioBlob);
//         setUploadedAudio(null); // Reset uploaded audio if a new recording is made
//         setAudioUrl(""); // Clear generated TTS audio
//       };

//       mediaRecorderRef.current.start();
//       setIsRecording(true);
//     } catch (error) {
//       console.error("Error accessing microphone:", error);
//     }
//   };

//   // Stop recording
//   const stopRecording = () => {
//     if (mediaRecorderRef.current) {
//       mediaRecorderRef.current.stop();
//       setIsRecording(false);
//     }
//   };

//   // Upload image & audio to FastAPI
//   const handleUpload = async () => {
//     if (!image) {
//       alert("Please select an image.");
//       return;
//     }

//     if (!audio && !uploadedAudio && !audioUrl) {
//       alert("Please record, upload an audio file, or generate TTS.");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("image", image);

//     if (uploadedAudio) {
//       formData.append("audio", uploadedAudio);
//     } else if (audio) {
//       formData.append("audio", audio, "recorded_audio.wav");
//     } else if (audioUrl) {
//       formData.append("text", text); // Send text for TTS-based lip-sync
//     }

//     try {
//       const response = await fetch("http://localhost:8000/generate_video/", {
//         method: "POST",
//         body: formData,
//       });

//       const data = await response.json();
//       if (data.video_url) {
//         setVideoUrl(data.video_url);
//       } else {
//         alert("Failed to generate video");
//       }
//     } catch (error) {
//       console.error("Upload error:", error);
//     }
//   };

//   return (
//     <div style={{ textAlign: "center", padding: "20px" }}>
//       <h1>Real-Time Lip-Sync Video Generator</h1>

//       {/* Image Upload */}
//       <h3>Upload Image:</h3>
//       <input type="file" accept="image/*" onChange={handleImageChange} />
//       <br /><br />

//       {/* Audio Upload */}
//       <h3>Upload Audio File:</h3>
//       <input type="file" accept="audio/*" onChange={handleAudioChange} />
//       <br /><br />

//       {/* Text-to-Speech Input */}
//       <h3>Or Convert Text to Speech:</h3>
//       <textarea
//         placeholder="Enter text to convert..."
//         value={text}
//         onChange={handleTextChange}
//         rows="3"
//         cols="40"
//       />
//       <br />
//       <button onClick={generateTTS} style={{ background: "orange", color: "white" }}>
//         Generate Speech
//       </button>
//       <br /><br />

//       {/* Play Generated Audio */}
//       {audioUrl && (
//         <div>
//           <h4>Generated Audio:</h4>
//           <audio controls>
//             <source src={audioUrl} type="audio/mpeg" />
//             Your browser does not support the audio tag.
//           </audio>
//         </div>
//       )}

//       {/* Audio Recording Controls */}
//       <h3>Or Record Audio:</h3>
//       {isRecording ? (
//         <button onClick={stopRecording} style={{ background: "red", color: "white" }}>
//           Stop Recording
//         </button>
//       ) : (
//         <button onClick={startRecording} style={{ background: "green", color: "white" }}>
//           Start Recording
//         </button>
//       )}

//       <br /><br />

//       {/* Upload and Process */}
//       <button onClick={handleUpload} style={{ background: "blue", color: "white" }}>
//         Generate Video
//       </button>

//       <br /><br />

//       {/* Display Video */}
//       {videoUrl && (
//         <div>
//           <h2>Generated Video:</h2>
//           <video controls width="400">
//             <source src={videoUrl} type="video/mp4" />
//             Your browser does not support the video tag.
//           </video>
//         </div>
//       )}
//     </div>
//   );
// };

// export default App;

import React, { useState, useRef } from "react";
import "./styles.css"; // Import the CSS file

const App = () => {
  const [image, setImage] = useState(null);
  const [imagePreview, setImagePreview] = useState("");
  const [audio, setAudio] = useState(null);
  const [uploadedAudio, setUploadedAudio] = useState(null);
  const [text, setText] = useState("");
  const [audioUrl, setAudioUrl] = useState("");
  const [videoUrl, setVideoUrl] = useState("");
  const [isRecording, setIsRecording] = useState(false);
  const [audioInputType, setAudioInputType] = useState("");
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);
  const [loading, setLoading] = useState(false);

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setImage(file);
      setImagePreview(URL.createObjectURL(file));
    }
  };

  const handleAudioChange = (event) => {
    setUploadedAudio(event.target.files[0]);
    setAudio(null);
    setAudioUrl("");
  };

  const handleTextChange = (event) => {
    setText(event.target.value);
  };

  const generateTTS = async () => {
    if (!text) {
      alert("Please enter text to convert to speech.");
      return;
    }

    try {
      const response = await fetch("http://localhost:8000/generate_audio/", {
        method: "POST",
        body: new URLSearchParams({ text }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
      });

      const data = await response.json();
      if (data.audio_url) {
        setAudioUrl(data.audio_url);
        setUploadedAudio(null);
      } else {
        alert("Failed to generate speech.");
      }
    } catch (error) {
      console.error("TTS error:", error);
    }
  };

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      mediaRecorderRef.current = new MediaRecorder(stream);
      audioChunksRef.current = [];

      mediaRecorderRef.current.ondataavailable = (event) => {
        audioChunksRef.current.push(event.data);
      };

      mediaRecorderRef.current.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: "audio/wav" });
        setAudio(audioBlob);
        setUploadedAudio(null);
        setAudioUrl(URL.createObjectURL(audioBlob));
      };

      mediaRecorderRef.current.start();
      setIsRecording(true);
    } catch (error) {
      console.error("Error accessing microphone:", error);
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
    }
  };

  const handleUpload = async () => {
    if (!image) {
      alert("Please select an image.");
      return;
    }

    if (!audio && !uploadedAudio && !audioUrl) {
      alert("Please record, upload an audio file, or generate TTS.");
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append("image", image);

    if (uploadedAudio) {
      formData.append("audio", uploadedAudio);
    } else if (audio) {
      formData.append("audio", audio, "recorded_audio.wav");
    } else if (audioUrl) {
      formData.append("text", text);
    }

    try {
      const response = await fetch("http://localhost:8000/generate_video/", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      if (data.video_url) {
        setVideoUrl(data.video_url);
      } else {
        alert("Failed to generate video");
      }
    } catch (error) {
      console.error("Upload error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container d-flex justify-content-center align-items-center">
      <div className="app-container">
        <h2 className="text-white text-center" style={{backgroundColor:"blue",color:"white",marginTop:"8px"}}>Real-Time Lip-Sync Generator</h2>

        <div className="form-group">
          <h3 style={{color:"white",marginTop:"5px"}}>Upload Image:</h3>
          <input type="file" accept="image/*" style={{marginLeft:"-50px",}} onChange={handleImageChange} />
          {imagePreview && <img src={imagePreview} alt="Uploaded" style={{ maxWidth: "530px", maxHeight: "400px",display:"flex",alignItems:"center",marginLeft:"120px"}} />}
        </div>

        <div className="form-group">
          <label style={{color:"white",width:"100px"}}>Select Audio Input:</label>
          <br></br>
          <select style={{width:"300px",backgroundColor:"",color:"black"}}onChange={(e) => setAudioInputType(e.target.value)}>
            <option value="">Choose...</option>
            <option value="upload">Upload Audio File</option>
            <option value="tts">Convert Text to Speech</option>
            <option value="record">Record Audio</option>
          </select>
        </div>

        {audioInputType === "upload" && <input type="file" accept="audio/*" onChange={handleAudioChange} style={{marginLeft:"-50px",marginTop:"5px"}}/>}
        {audioInputType === "tts" && <><textarea value={text} style={{width:"300px",height:"100px",marginTop:"5px"}}onChange={handleTextChange} placeholder="Enter text more than 3 words ..."/><button style={{backgroundColor:"blue",color:"white"}}onClick={generateTTS}>Generate Speech</button></>}
        {audioInputType === "record" && (isRecording ? <button onClick={stopRecording}style={{backgroundColor:"blue",color:"white"}}>Stop Recording</button> : <button style={{backgroundColor:"blue",color:"white"}} onClick={startRecording}>Click to Start Recording</button>)}

        {audioUrl && <audio controls src={audioUrl} />}

        <button style={{backgroundColor:"blue",color:"white",}} onClick={handleUpload} disabled={loading}>{loading ? "Generating..." : "Generate Video"}</button>
        {videoUrl && <video controls src={videoUrl} width="100%" height="100%" />}
      </div>
    </div>
  );
};

export default App;
