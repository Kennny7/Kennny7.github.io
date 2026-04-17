export interface GitHubRepoData {
  stars: number;
  forks: number;
  language: string;
  description: string | null;
  updatedAt: string;
}

export async function fetchGitHubRepo(repoUrl: string): Promise<GitHubRepoData | null> {
  try {
    // Extract owner/repo from URL like https://github.com/Kennny7/repo-name
    const match = repoUrl.match(/github\.com\/([^/]+)\/([^/]+)/);
    if (!match) return null;
    const [, owner, repo] = match;
    
    const response = await fetch(`https://api.github.com/repos/${owner}/${repo}`);
    if (!response.ok) return null;
    
    const data = await response.json();
    return {
      stars: data.stargazers_count,
      forks: data.forks_count,
      language: data.language,
      description: data.description,
      updatedAt: data.updated_at,
    };
  } catch (error) {
    console.warn(`Failed to fetch GitHub data for ${repoUrl}:`, error);
    return null;
  }
}