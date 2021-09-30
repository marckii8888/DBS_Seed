import React, {useState} from "react";
import ReactDOM from "react-dom";
import CategoryComponent1 from "./CategoryComponent1.js";
import CategoryComponent2 from "./CategoryComponent2.js";
import CategoryComponent3 from "./CategoryComponent3.js";
import categories from '../datajson/categories.json';
import products from '../datajson/products.json';
import productsapi from '../api/products';

const Home = () => { 
    
    useEffect(() => {
        // const findProduct = productlist.filter(product => product.id == id);
        // setProduct(findProduct[0]);
        // console.log(product);
    });

    // const categorieslist = 
    
    // renderedList = () => {
    //     const x = categories.map(category => {
    //         products.filter(product => product.category_id === category.id)
    //     })
    // }


    return( <div>
        <CategoryComponent1/> 
        <CategoryComponent2/>
        <CategoryComponent3/>  
    </div> )
}

export default Home;