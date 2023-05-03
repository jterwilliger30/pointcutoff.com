import React, { useState, useEffect } from "react"
import axios from 'axios'

function Create() {

    const [mos, setTitle] = useState('11b')
    const [ac_agr, setSelector] =  useState('ac')

    useEffect(() => {
        axios.get("mos_list", {}).then((getResponse) => {
            console.log(getResponse.data);
            var i
            var x = ''
            for (i in getResponse.data) {
                x += "<option value=\"" + getResponse.data[i] + "\">" + getResponse.data[i] + "</option>"
            }
            document.getElementById('mos_list').innerHTML = x;
        }

        )
    },[]);
        

    const handleSubmit = (e) => {
        e.preventDefault()
        const myParams = {data: mos, selector: ac_agr}

        console.log(ac_agr);

        axios.post("handle_data", myParams).then((getResponse) => {
            console.log(getResponse.data);
            var i
            var x = ''
            for (i in getResponse.data) {
                x += "<h2>" + i + ": " + "<span class=\"nums\">" + getResponse.data[i] + "</span>" + "</h2>"
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

        <select onChange={(e) => setTitle(e.target.value)} id="mos_list">
            
        </select>

        <button type="submit">Submit</button>
        <select value={ac_agr} onChange={(e) => setSelector(e.target.value)} id="selector">
            <option value="ac">Active Component</option>
            <option value="agr">National Guard / Reserve</option>
        </select> <hr />
        <h1>Current results are for <span class="month">May, 2023</span>.</h1>
        <p id="demo"></p>
	<p id="footer">
	<a href="https://github.com/jterwilliger30/pointcutoff.com">GitHub Repo</a>  <br />
	<a href="mailto:jterwilliger30@gmail.com">Email for questions & feature requests</a>
	</p>
    <h4 id="disclaimer">This site is not affiliated with or a reflection on the Department of Defense.</h4>
        </form>)
       
}
export default Create;
