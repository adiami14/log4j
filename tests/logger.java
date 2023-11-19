import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;

public class LoggerServlet extends HttpServlet {
    private static final Logger logger = LogManager.getLogger(LoggerServlet.class);

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        String logData = request.getParameter("logData");
        logger.error(logData != null ? logData : "[no data provided to log]");
    }
}
