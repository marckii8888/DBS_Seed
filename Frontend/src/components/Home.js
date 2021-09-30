import React, {useState} from "react";
import ReactDOM from "react-dom";
import CategoryComponent1 from "./CategoryComponent1.js";
import CategoryComponent2 from "./CategoryComponent2.js";
import CategoryComponent3 from "./CategoryComponent3.js";

const Home = () => { 
    
    return( <div>
        <CategoryComponent1/> 
        <CategoryComponent2/>
        <CategoryComponent3/>  
    </div> )
}

export default Home;