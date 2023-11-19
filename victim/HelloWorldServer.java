import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;
import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;
import java.util.Map;


public class HelloWorldServer {
    private static final Logger logger = LogManager.getLogger(HelloWorldServer.class);

    public static void main(String[] args) throws IOException {
        int port = Integer.parseInt(args[0]);
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);
        server.createContext("/", new HelloHandler());
        server.start();
        
        System.out.println("Server is running on http://localhost:" + port);
    }
    
    static class HelloHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            // Get the query parameters from the request URI
            String query = exchange.getRequestURI().getQuery();
            Map<String, String> queryParams = QueryString.parse(query);
            
            // Extract the "name" parameter from the query parameters
            String name = queryParams.getOrDefault("name", "World");
            
            // Prepare the personalized greeting
            String response = "Hello, " + name + "!";
            
            // Log the name using the logger
            logger.error(query);
            
            // Get the response output stream
            OutputStream outputStream = exchange.getResponseBody();
            
            // Set the response headers
            exchange.sendResponseHeaders(200, response.length());
            
            // Write the response content
            outputStream.write(response.getBytes());
            
            // Close the output stream
            outputStream.close();
        }
    }
    
    // Helper class to parse query strings
    static class QueryString {
        public static Map<String, String> parse(String query) {
            // Implement query string parsing logic here
            // This is a simplified example
            // You might want to use a library or more robust parsing
            return java.util.Arrays.stream(query.split("&"))
                    .map(param -> param.split("="))
                    .collect(java.util.stream.Collectors.toMap(param -> param[0], param -> param[1]));
        }
    }
}
