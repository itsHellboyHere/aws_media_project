import {QueryClient, QueryClientProvider} from "@tanstack/react-query"
import PostsPage from "./pages/PostsPage";
const queryClient = new QueryClient();
const App = function(){
  return (
      <PostsPage/>
  )
}
export default App;