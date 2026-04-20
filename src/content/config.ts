import { defineCollection, z } from 'astro:content';

const projectsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    image: z.string().optional(),
    github: z.string().url(),
    demo: z.string().url().optional(),
    tags: z.array(z.string()).default([]),
    featured: z.boolean().default(true),
    fetchGithubData: z.boolean().default(false), 
  }),
});

export const collections = {
  'projects': projectsCollection,
};