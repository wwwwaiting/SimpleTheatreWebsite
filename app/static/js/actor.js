/* actor.js - Theatre blocking JavaScript */
"use strict";
console.log('actor.js')  // log to the JavaScript console.

// Function to remove all blocking parts from current window
function removeAllBlocks() {
	blocks.innerHTML = ''
}

/* Function to add a blocking part to browser window */
function addScriptPart(scriptText, startChar, endChar, position) {
	const scriptPartText = scriptText.slice(startChar, endChar + 1);
	const part = blocks.children.length + 1

	const html = `<h4>Part ${part}</h4>
          <p><em>"${scriptPartText}"</em></p>
          <p>Stage Position: <strong>${position}</strong></p>`

    const block = document.createElement('div'); block.className = 'col-lg-12';
    block.innerHTML = html;
    blocks.appendChild(block)
}

// Function to add the example block (when clicking the example block button)
function getExampleBlock() {
	const url = '/example';

	// A 'fetch' AJAX call to the server.
    fetch(url)
    	.then((res) => { 
    		//// Do not write any code here
	        return res.json()
	        //// Do not write any code here
	    })
	    .then((jsonResult) => {
	    	// This is where the JSON result (jsonResult) from the server can be accessed and used.
	        console.log('Result:', jsonResult)
	        // Use the JSON to add a script part
	        addScriptPart(jsonResult[0], jsonResult[1], jsonResult[2], jsonResult[3])
	    }).catch((error) => {
	    	// if an error occured it will be logged to the JavaScript console here.
	        console.log("An error occured with fetch:", error)
	    })	
}


/* Write the code to get the blocking for a particular script and actor */
function getBlocking() {
	// Remove any existing blocks
	removeAllBlocks();

	// Get the script and actor numbers from the text box.
	const scriptNumber = scriptNumText.value;
	const actorNumber = actorText.value;
	console.log(`Get blocking for script number ${scriptNumber} for actor ${actorNumber}`);
	const block = document.createElement('div'); block.className = 'col-lg-12';

	/* Add code below to get JSON from the server and display it appropriately. */
	const url = '/script/' + scriptNumber;

	if (scriptNumber === '' || actorNumber === ''){
		//display message if missing input attribute
		const html = `Please enter Script number and Actor number to get blocking information.`
	    block.innerHTML = html;
	    blocks.appendChild(block)
	}
	else{
		// A 'fetch' AJAX call to the server.
	    fetch(url)
	    	.then((res) => { 
		        return res.json()
		    })
		    .then((jsonResult) => {
		    	// This is where the JSON result (jsonResult) from the server can be accessed and used.
		        console.log('Result:', jsonResult);
		        // Use the JSON to add a script part
		        // do nothing if there is not script for scriptNumber
		        if (Object.keys(jsonResult).length !==0){
			        let line = jsonResult['line'];
			        let valid_parts = Object.keys(jsonResult).filter(key=>key.includes('part'))
			        	.filter(key=>jsonResult[key]['actor_blocks'].hasOwnProperty(actorNumber));
			        if (valid_parts.length === 0){
		        		const html = `Please enter valid Actor number for the script.`
	    				block.innerHTML = html;
	    				blocks.appendChild(block)
			        }
			        else{
			        	valid_parts.forEach(result => addScriptPart(line, jsonResult[result]['start_idx'], 
			        		jsonResult[result]['end_idx'], jsonResult[result]['actor_blocks'][actorNumber]));
		        	}
		        }
		        else{
		        	const html = `Please enter valid Script number.`
	    			block.innerHTML = html;
	    			blocks.appendChild(block)
		        }

		    }).catch((error) => {
		    	// if an error occured it will be logged to the JavaScript console here.
		        console.log("An error occured with fetch:", error)
		    })
	}

}

