import java.util.*;
class abc
{
    static int wordladder(String start,String target,ArrayList<String> al)
    {
        HashSet<String> hs=new HashSet<>(al);
        if(!hs.contains(target)) return 0;
        Queue<String> q=new LinkedList<>();
        q.add(start);
        int level=1;
        while(!q.isEmpty())
        {
            int count=q.size();
            for(int i=0;i<count;i++)
            {
                String curr=q.poll();
                char a[]=curr.toCharArray();
                for(int j=0;j<a.length;j++)
                {
                    char original_char=a[j];
                    for(char c='a';c<='z';c++)
                    {
                        if(a[j]==c) continue;
                        a[j]=c;
                        String new_string=new String(a);
                        if(new_string.equals(target)) return level+1;
                        if(hs.contains(new_string))
                        {
                            q.add(new_string);
                            hs.remove(new_string);
                        }
                    }
                    a[j]=original_char;
                }
            }
            level++;
        }
        return 0;
    }
    public static void main(String[] args) {
        String start,target;
        Scanner sc=new Scanner(System.in);
        start=sc.next();
        target=sc.next();
        int n=sc.nextInt();
        ArrayList<String> al=new ArrayList<>();
        for(int i=0;i<n;i++)
        al.add(sc.next());
        System.out.println(wordladder(start, target, al));
        sc.close();
    }
}