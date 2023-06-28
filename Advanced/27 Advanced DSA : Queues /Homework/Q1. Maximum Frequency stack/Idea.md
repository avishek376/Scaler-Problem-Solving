Pushing into a stack looks like this:
    void push(int x)
    {
        freq[x]++;
        if(freq[x] > max_freq) max_freq = freq[x];
    
        if(stacks.count(freq[x]))
        {
            stacks[freq[x]].push(x);    
        }
        else
        {
            stack st;
            st.push(x);
            stacks[freq[x]] = st;
        }
    }
This helps in maintaining the required answer and getting the answer to each of the 
parts that need to be done such as push and pop of the elements</pre>

    TC: O(N)
    SC: O(K)
