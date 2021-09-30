import React from 'react';

const ShoppingCart = () => {

    return (
        <div class="row">
            <label>
				My Cart 
			</label>
            <div class="form-group col-sm-12 col-md-12">
                <div class="col-sm-7 col-md-7">
                    <table id="cartTable">
                        <thead>
                            <tr>
                                <th>Quantity</th>
                                <th>Item</th>
                                <th>Price</th>
                                <th>Edit</th>
                                <th>Delete</th>
                            </tr>
                        </thead>
                        <tbody id="cartDataBody">
        
                        </tbody>
                    </table>
                </div>
                <div class="col-sm-5 col-md-5">
                    <label>
                        Total
                    </label>
                    <table id="totalTable">
                        <thead>
                            <tr>
                                <th>Total Price</th>
                                <th></th>
                            </tr>
                        </thead>
                        <tbody id="totalBody">
        
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    )
}

export default ShoppingCart;