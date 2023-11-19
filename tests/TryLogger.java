import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;
 
public class Gday {
   static Logger logger = LogManager.getLogger(Gday.class);
 
   public static void main(String... args) {
      System.out.println("Main says, 'Hello, world.'");
      logger.error(args.length > 0 ? args[0] : "[no data provided to log]");
      System.out.println("Main is exiting.");
   }
}


