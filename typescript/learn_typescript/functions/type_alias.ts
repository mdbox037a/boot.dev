type SupportResponse = (name: string) => string;

export function greetCustomer(name: SupportResponse): string {
  return `Hello ${name}, welcome to Support.ai! How can I assist you today?`;
}

export function farewellCustomer(name: SupportResponse): string {
  return `Goodbye ${name}, have a great day!`;
}
