import React, { useState } from 'react';

const Login = ({setIsLoggedIn}) => {

    const [loginID, setLoginID] = useState('');
    const [password, setPassword] = useState('');

    const onLoginIDChange = (e) => { setLoginID(e.target.value);}
    const onPasswordChange = (e) => { setPassword(e.target.value);}

    const attemptLogin = async () => {
        // call api to send the login and pw
        // if success, setIsLoggedIn(true)
        // const response = await apicall.post('/loginroute_whateveritis', {loginID, password})
        // if (response) {setIsLoggedIn(true);}
    };

    return (        
        <div className="ui middle aligned grid">
            <div className="eight column wide">
                <form className="ui form" onSubmit={attemptLogin}>
                    <div className="field">
                        <label>Login ID</label>
                        <input value={loginID} onChange={onLoginIDChange}/>
                    </div>
                    <div className="field">
                        <label>Password</label>
                        <input value={password} onChange={onPasswordChange}/>
                    </div>
                    <button type="submit" className="ui button red">Submit</button>
                </form>
            </div>
            
        </div>
        // <Route 
        //     {...rest} 
        //     render={props => isLoggedIn? <Component {...props} /> : <Redirect to="/login"/>}
        // />
    );
}

export default Login;