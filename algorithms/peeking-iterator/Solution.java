/**
 * Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].
 
 * Call next() gets you 1, the first element in the list.
 
 * Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.
 
 * You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.
 *
 */

// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {
    Integer next;
    Iterator<Integer> iter;
    public PeekingIterator(Iterator<Integer> iterator) {
        // initialize any member here.
        if(iterator.hasNext()){
            this.next=iterator.next();
            this.iter=iterator;
        }else{
            this.next=null;
            this.iter=iterator;
        }
    }
    
    // Returns the next element in the iteration without advancing the iterator.
    public Integer peek() {
        return this.next;
    }
    
    // hasNext() and next() should behave the same as in the Iterator interface.
    // Override them if needed.
    @Override
    public Integer next() {
        Integer prev=this.next;
        if(this.iter.hasNext()){
            this.next=this.iter.next();
        }else{
            this.next=null;
        }
        return prev;
    }
    
    @Override
    public boolean hasNext() {
        if(next==null){
            return false;
        }
        return true;
    }
}