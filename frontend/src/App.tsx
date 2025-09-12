import { useState } from 'react';

function App() {
  

  // const [name , setName] = useState('');

  // function handleChange(e: React.ChangeEvent<HTMLInputElement>) {
  //   console.log("handleChange function is called and the e.target.value is ", e.target.value)
  //   setName(e.target.value)
  // }

  // function handleSubmit(e: React.FormEvent<HTMLFormElement>){
  //   e.preventDefault();
  //   // when i click on the submit button 
  //   alert("Form submitted and name is " + name)
  //   console.log("handleSubmit function is called and the name is ", name)
  // }

  const [first_number , setFirst_number] = useState("");
  const [second_number , setSecond_number] = useState("");
  const [result , setResult] = useState < number | null > (null);


  function handleChange_1(e: React.ChangeEvent<HTMLInputElement>)
  {
    setFirst_number(e.target.value)
  }
  function handleChange_2(e: React.ChangeEvent<HTMLInputElement>)
  {
    setSecond_number(e.target.value)
  }

  
  async function handleSubmit(e: React.FormEvent){
    e.preventDefault(); // this line of code prevent reloading the page after submitting 
    const res = await fetch("http://localhost:8000/api/add" , {
      method : 'POST' , 
      headers : {
        "Content-Type" : "Application/json"
      }, 
      body : JSON.stringify({
        "a" : first_number , 
        "b" : second_number
      })
    });

    console.log("request sent");
    const data = await res.json();
    console.log("request received");

    setResult(data.sum);
  }


  return (
    <div>
      <h1>Welcome again</h1>
      
      <form onSubmit={handleSubmit}>
        <input 
        type = "number"
        value = {first_number}
        onChange = {handleChange_1}
        placeholder = "Enter the first number"
        />
        <br/>
        <input 
        type = "number"
        value = {second_number}
        onChange = {handleChange_2}
        placeholder = "Enter the second number"
        />
        <button type = "submit">Submit GO</button>

        <h1>the sum is {result}</h1>
      </form>

    </div>
  );
}

export default App;