class javaThread extends Thread 
{
    public static void main(String [] args) 
    {
    	javaThread t = new javaThread();
        t.start();
        System.out.print("cse. ");
        t.start();
        System.out.print("amrita. ");
    }
    public void run() 
    {
        System.out.print("students ");
    }
}