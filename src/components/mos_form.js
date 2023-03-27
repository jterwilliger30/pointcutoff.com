import React, { useState } from "react"
import axios from 'axios'

function Create() {
    const [mos, setTitle] = useState('')
    const handleSubmit = (e) => {
        e.preventDefault()
        const myParams = {data: mos}

        axios.post("handle_data", myParams).then((getResponse) => {
            console.log(getResponse.data);
            var i
            var x = ''
            for (i in getResponse.data) {
                x += "<h2>" + i + "<span class=\"nums\">" + getResponse.data[i] + "</span>" + "</h2>"
            }
            console.log(x)
            document.getElementById('demo').innerHTML = x
          }).catch(function(error) {
            console.log("MOS DNE")
            var x = 'MOS does not exist in our records :('
            document.getElementById('demo').innerHTML = x
          }
            )
    }

    return (
        <form onSubmit={handleSubmit} method="post">

        <label>MOS:</label>
        <input
        type="text"
        value={mos}
        required
        onChange={(e) => setTitle(e.target.value)}
        >

        </input>
        <button type="submit">Submit</button>
        <h1>Current results are for <span class="month">April, 2023</span>.</h1>
        <p id="demo"></p>
	<p id="footer">
	<a href="https://github.com/jterwilliger30/pointcutoff.com">GitHub Repo</a>  <br />
	<a href="mailto:jterwilliger30@gmail.com">Email for questions & feature requests</a>
	</p>
        </form>

        
    )
       


}
export default Create;
